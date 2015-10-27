from MesoPy import Meso, MesoPyError
from nose.tools import *

m = Meso(api_token='3428e1e281164762870915d2ae6781b4')

# Basic Function Tests
def testvarlistfunc():
    var_list = m.variable_list()
    ok_(var_list)


def teststationsfunc():
    stations = m.station_list(state='CO', county='Larimer')
    ok_('KFNL' == stations['STATION'][1]['STID'])


def testtimeseriesfunc():
    timeseries = m.timeseries_obs(stid='kfnl', start='201504261800', end='201504262300')
    ok_(timeseries)


def testclimatologyfunc():
    climatology = m.climatology_obs(stid='kden', startclim='04260000', endclim='04270000', units='precip|in')
    ok_(climatology)


def testprecipfunc():
    precip = m.precipitation_obs(stid='kfnl', start='201504261800', end='201504271200', units='precip|in')
    ok_(precip)


# Miscellaneous Tests
def testvarexists():
    var_list = m.variable_list()
    ok_('relative_humidity' in var_list['VARIABLES'])


def testlateststrlist():
    latest = m.latest_obs(stid=['kfnl', 'kden', 'ksdf'])
    eq_(len(latest['STATION']), 3)


# Error Handling
@raises(MesoPyError)
def testbadurlstring():
    latest = m.latest_obs(stid='')
    print(latest)


@raises(MesoPyError)
def testauth():
    badtoken = Meso(api_token='3030')
    badtoken.latest_obs(stid=['kfnl', 'kden', 'ksdf'])


@raises(MesoPyError)
def testgeoparms():
    m.precipitation_obs(start='201504261800', end='201504271200', units='precip|in')