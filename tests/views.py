from datetime import datetime, timedelta

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from tests.models import Comparison


def statistics(path):
    results = {'path': path}
    missing = []
    seconds1 = []
    seconds2 = []
    total = per_hour = errors = failures = 0
    one_hour_ago = datetime.now() - timedelta(hours=1)
    query = Comparison.all().filter('path', path).order('-timestamp')
    for comparison in query.fetch(200):
        if not comparison.path or not comparison.path.startswith(path):
            continue
        total += 1
        if comparison.message == 'error':
            errors += 1
        elif comparison.message:
            failures += 1
        if comparison.timestamp > one_hour_ago:
            per_hour += 1
        if comparison.missing1:
            missing.append(comparison.missing1)
        if comparison.missing2:
            missing.append(comparison.missing2)
        seconds1.append(comparison.seconds1)
        seconds2.append(comparison.seconds2)
    results['total'] = total
    results['per_hour'] = per_hour
    if not total:
        results['error_percent'] = 0.0
        results['failure_percent'] = 0.0
        return results
    results['error_percent'] = 100.0 * errors / total
    results['failure_percent'] = 100.0 * failures / total
    missing.sort()
    if missing:
        results['missing_max'] = max(missing)
        results['missing_median'] = max(missing[len(missing) / 2])
    seconds1.sort()
    seconds2.sort()
    results['seconds1_max'] = max(seconds1)
    results['seconds2_max'] = max(seconds2)
    results['seconds1_median'] = seconds1[len(seconds1) / 2]
    results['seconds2_median'] = seconds2[len(seconds2) / 2]
    return results


def index(request):
    statistics_list = [
        statistics('/domains/descending/'),
        ]
    return render_to_response(request, 'tests/index.html', locals())


def detail(request, path):
    query = Comparison.all().filter('path', path).order('-timestamp')
    comparisons_list = query.fetch(100)
    return render_to_response(request, 'tests/detail.html', locals())
