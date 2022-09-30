%undefine _debugsource_packages
%define module	chaco

Summary:	Enthought Tool Suite - interactive 2D plotting
Name:		python-%{module}
Version:	4.5.0
Release:	5.1
Source0:	https://www.enthought.com/repo/ets/chaco-%{version}.tar.gz
License:	BSD
Group:		Development/Python
URL:		https://github.com/enthought/chaco/
Obsoletes:	python-enthought-chaco
Obsoletes:	python-enthought-chaco2
Requires:	python-traits >= 4.2.0
Requires:	python-enable >= 4.2.0
Requires:	python2-numpy >= 1.1.0
Requires:	python-reportlab
BuildRequires:	python2-numpy atlas
BuildRequires:	python-devel
#BuildRequires:	python-traits >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
#BuildRequires:	x11-server-xvfb, procps
#BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx environment-modules
BuildRequires:	pkgconfig

%description
Chaco is a Python plotting application toolkit that facilitates
writing plotting applications at all levels of complexity, from simple
scripts with hard-coded data to large plotting programs with complex
data interrelationships and a multitude of interactive tools. While
Chaco generates attractive static plots for publication and
presentation, it also works well for interactive data visualization
and exploration.

%prep
%setup -q -n %{module}-%{version}

%build
python2 setup.py build
#python2 setup.py build_docs

%install
python2 setup.py install --root=%{buildroot}

%files
%doc *.txt *.rst examples/ docs/*.pdf
%{python2_sitearch}/%{module}*

%changelog
* Mon Feb 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5.0
- Rebuilt for Fedora
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814714
- Update to 4.2.0.
* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745667
- Update to 4.1.0.
* Fri Sep 02 2011 Lev Givon <lev@mandriva.org> 4.0.1-1
+ Revision: 697901
- Update to 4.0.1.
* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689214
- import python-chaco
