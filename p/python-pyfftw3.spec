%undefine _debugsource_packages
%define modname PyFFTW3

Name:           python-pyfftw3
Version:        0.2.1
Release:        3.1
Summary:        A python binding to the FFTW3 library
URL:            https://pypi.python.org/pypi/PyFFTW3
License:        GPLv3
Group:          Development/Libraries/Python
Source:         %{modname}-%{version}.tar.gz
BuildArch: noarch
BuildRequires:  python-devel fdupes
BuildRequires:  fftw3-devel

%description
PyFFTW are python bindings for the FFTW3 (fastest Fourier transform in the West)
C-library written in python ctypes.

Authors:
--------
Jochen Schroeder <cycomanic _AT_ gmail _DOT_ com>
Pearu Peterson <pearu.peterson _AT_ gmail _DOT_ com>

%prep
%setup -q -n %{modname}-%{version}
 
%build
export CFLAGS="$RPM_OPT_FLAGS"
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files
%doc AUTHORS COPYING README.txt
%{python2_sitelib}/*

%changelog
* Wed Dec 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora

* Mon Jan 24 2011 scorot@gtt.fr - 0.2.1
- Initial release
