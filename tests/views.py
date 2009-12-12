from datetime import datetime, timedelta

from ragendja.template import render_to_response
from ragendja.dbutils import get_object_or_404

from tests.models import Comparison


def statistics(path):
    results = {'path': path}
    missing = []
    seconds1 = []
    seconds2 = []
    total = errors = failures = 0
    one_day_ago = datetime.now() - timedelta(hours=24)
    query = Comparison.all().filter('path', path).order('-timestamp')
    for comparison in query.fetch(400):
        if not comparison.path or not comparison.path.startswith(path):
            continue
        if comparison.message and 'message' not in results:
            results['message'] = comparison.message
        total += 1
        if comparison.message == 'error':
            errors += 1
        elif comparison.message:
            failures += 1
        if comparison.missing1:
            missing.append(comparison.missing1)
        if comparison.missing2:
            missing.append(comparison.missing2)
        if comparison.seconds1:
            seconds1.append(comparison.seconds1)
        if comparison.seconds2:
            seconds2.append(comparison.seconds2)
    results['total'] = total
    if not total:
        results['error_percent'] = 0.0
        results['failure_percent'] = 0.0
        return results
    results['error_percent'] = 100.0 * errors / total
    results['failure_percent'] = 100.0 * failures / total
    missing.sort()
    if missing:
        results['missing_min'] = min(missing)
        results['missing_median'] = missing[len(missing) / 2]
        results['missing_max'] = max(missing)
    seconds1.sort()
    seconds2.sort()
    results['seconds1_min'] = min(seconds1)
    results['seconds2_min'] = min(seconds2)
    results['seconds1_median'] = seconds1[len(seconds1) / 2]
    results['seconds2_median'] = seconds2[len(seconds2) / 2]
    results['seconds1_max'] = max(seconds1)
    results['seconds2_max'] = max(seconds2)
    return results


def index(request):
    statistics_list = [
        statistics('/domains/descending/'),
        statistics('/dns/descending/'),
        ]
    return render_to_response(request, 'tests/index.html', locals())


def detail(request, path):
    query = Comparison.all().filter('path', path).order('-timestamp')
    comparisons_list = query.fetch(100)
    return render_to_response(request, 'tests/detail.html', locals())
