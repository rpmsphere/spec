%define pyname pymc

Name:           python2-%{pyname}
Version:        2.2alpha.dev2114
Release:        7.1
Summary:        Markov chain Monte Carlo for Python
License:        MIT
URL:            http://code.google.com/p/pymc/downloads/list
Group:          Development/Libraries/Python
Source0:        %{pyname}-2114.tar.bz2
BuildRequires:  python2-devel, python2-setuptools, python2-numpy
BuildRequires:  gcc-gfortran, numpy-f2py, atlas-devel
Requires:       python2-numpy

%description
Bayesian estimation, particularly using Markov chain Monte Carlo (MCMC), is an
increasingly relevant approach to statistical estimation. However, few
statistical software packages implement MCMC samplers, and they are non-trivial
to code by hand. PyMC is a python module that implements the Metropolis-Hastings
algorithm as a python class, and is extremely flexible and applicable to a large
suite of problems. PyMC includes methods for summarizing output, plotting,
goodness-of-fit and convergence diagnostics.

%prep
%setup -q -n %{pyname}
sed -i -e '/from __future__ import with_statement/d' -e '2i from __future__ import with_statement' pymc/tests/test_adaptive.py
sed -i '1204s|work|dble(work)|' pymc/gibbsit.f

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT \
                                            --record=INSTALLED_FILES
%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CREDITS.rst LICENSE README.rst DEVELOPERS.txt
%{python2_sitearch}/%{pyname}*

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2alpha
- Rebuild for Fedora
* Mon Dec  5 2011 ocefpaf@gmail.com
- updated to revision 2114
* Sat Oct 15 2011 ocefpaf@gmail.com
- updated to version 2.2alpha ; revision 2104
* Sat Dec 18 2010 ocefpaf@yahoo.com.br
- first OpenSuse release
