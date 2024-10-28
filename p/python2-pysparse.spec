Name:           python2-pysparse
Version:        1.2
Release:        16.1
Summary:        A fast sparse matrix library for Python
Group:          Development/Libraries/Python
License:        BSD
URL:            https://pysparse.sourceforge.net/index.html
Source0:        pysparse-%{version}-dev213.tar.bz2
Patch0:         pysparse-1.2-fix-implicit-definitions.patch
Patch1:         pysparse-1.2-fix-no-return-in-nonvoid-function.patch
BuildRequires:  python2-devel python2-numpy atlas-devel python2-setuptools environment-modules
#BuildRequires:  python2-sphinx python2-pygments

%description
Pysparse is a fast sparse matrix library for Python. It provides several sparse
matrix storage formats and conversion methods. It also implements a number of
iterative solvers, preconditioners, and interfaces to efficient factorization
packages. Both low-level and high-level interfaces are available, each with
different strengths.

%prep
%setup -q -n pysparse-%{version}-dev213
%patch 0 -p1
%patch 1 -p1

%build
export CFLAGS=-Wno-format-security
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --prefix %{_prefix} --root $RPM_BUILD_ROOT

# fix executables permissions
find $RPM_BUILD_ROOT%{python2_sitearch}/pysparse -type f -name *.py -exec %__chmod 755 {} \;
%__chmod 755 $RPM_BUILD_ROOT%{python2_sitearch}/pysparse/sparse/*sparseMatrix.py 

# build doc
#export PYTHONPATH=$RPM_BUILD_ROOT%{python2_sitearch}
#make -C doc/pysparse PAPER=letter html
#rm -f doc/pysparse/build/html/.buildinfo

find $RPM_BUILD_ROOT%{python2_sitearch} -type f -name *.pyc -exec %__sed -i 's|$RPM_BUILD_ROOT||g' {} \;

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{python2_sitearch}/pysparse/*.py %{buildroot}%{python2_sitearch}/pysparse/*/*.py
 
%files
%doc CHANGES LICENSE README TODO examples test
%{python2_sitearch}/*

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Sat Apr 02 2011 scorot@gtt.fr
- Fix no-return-in-non-void-function
* Fri Apr 01 2011 scorot@gtt.fr
- first package
