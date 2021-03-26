Name:           python-lz4
Version:        0.6.1
Release:        5.1
URL:            https://github.com/steeve/python-lz4
Summary:        LZ4 Bindings for Python
License:        GPLv2+
Group:          Development/Languages/Python
Source:         https://pypi.python.org/packages/source/l/lz4/lz4-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose

%description
This package provides bindings for the lz4 compression library by Yann Collet.

%prep
%setup -q -n lz4-%{version}

%build
export CFLAGS="%{optflags}"
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc README.rst
%{python_sitearch}/*

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
* Fri Mar 21 2014 Antoine Martin <antoine@devloop.org.uk - 0.6.1-0
- New upstream release
* Wed Jan 15 2014 Antoine Martin <antoine@devloop.org.uk - 0.6.0-1.0
- Fix version in specfile
- build debuginfo packages
* Sun Dec 8 2013 Stephen Gauthier <sgauthier@spikes.com> - 0.6.0-0
- First version for Fedora Extras
