%undefine _debugsource_packages
%define modname Pyevolve

Name:           python-pyevolve
Version:        0.6rc1
Release:        14.1
Summary:        Genetic Algorithms in Python
URL:            https://pyevolve.sourceforge.net/
License:        BSD
Group:          Development/Libraries/Python
Source:         %{modname}-%{version}.tar.bz2
#BuildRequires:  python-sphinx environment-modules
BuildRequires:  python-pygments python2-setuptools
BuildRequires:  numpy python-matplotlib graphviz atlas-devel
Requires:       numpy 
BuildArch:      noarch
BuildRequires:  netpbm

%description
Pyevolve is a complete genetic algorithm framework written in pure python.

%prep
%setup -q -n %{modname}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build
#cd docs 
#chmod +x ./build_docs.sh
#./build_docs.sh

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

# make some clean up to silent rpmlint
#cd docs
#mv build html
#rm -rf html/.buildinfo html/.doctrees

# fix line end encoding
#find html/ -type f -exec %__sed -i 's/\r//' {} \;
#sed -i 's/\r//' $RPM_BUILD_ROOT/%{_bindir}/pyevolve_graph.py

# Add missing shebang
%__sed -i -e '1i#!/usr/bin/python2' $RPM_BUILD_ROOT/%{_bindir}/pyevolve_graph.py

%files
#doc docs/html
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6rc1
- Rebuilt for Fedora
* Sat Mar 19 2011 scorot@gtt.fr - 0.6rc1
- Initial release
