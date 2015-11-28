#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module	pyramid
Summary:	The Pyramid web application development framework, a Pylons project
Name:		python-%{module}
Version:	1.4
Release:	2
License:	BSD-derived (http://www.repoze.org/LICENSE.txt)
Group:		Libraries/Python
Source0:	http://pypi.python.org/packages/source/p/pyramid/%{module}-%{version}.tar.gz
# Source0-md5:	d72b664cf3852570faa44a81eb0e448b
URL:		http://www.pylonsproject.org/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with tests}
BuildRequires:	python-PasteDeploy >= 1.5.0
%endif
Requires:	Zope-Deprecation >= 3.5.0
Requires:	Zope-Interface >= 3.8.0
Requires:	python-Mako >= 0.3.6
Requires:	python-PasteDeploy >= 1.5.0
Requires:	python-WebOb >= 1.2
Requires:	python-chameleon >= 1.2.3
Requires:	python-distribute
Requires:	python-modules
Requires:	python-repoze.lru >= 0.4
Requires:	python-translationstring >= 0.4
Requires:	python-venusian >= 1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# solve this: http://lists.pld-linux.org/mailman/pipermail/pld-devel-en/2013-January/023404.html
%define		_noautoreq	'pythonegg\\(webob\\)'

%description
Pyramid is a small, fast, down-to-earth, open source Python web
application development framework. It makes real-world web application
development and deployment more fun, more predictable, and more
productive.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/tests

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BFG_HISTORY.txt CHANGES.txt HACKING.txt HISTORY.txt LICENSE.txt README.rst TODO.txt
%attr(755,root,root) %{_bindir}/bfg2pyramid
%attr(755,root,root) %{_bindir}/pcreate
%attr(755,root,root) %{_bindir}/prequest
%attr(755,root,root) %{_bindir}/proutes
%attr(755,root,root) %{_bindir}/pserve
%attr(755,root,root) %{_bindir}/pshell
%attr(755,root,root) %{_bindir}/ptweens
%attr(755,root,root) %{_bindir}/pviews
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/config
%{py_sitescriptdir}/%{module}/fixers
%{py_sitescriptdir}/%{module}/scaffolds
%{py_sitescriptdir}/%{module}/scripts
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
