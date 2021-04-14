Name:           python3-xpybutil
Version:        0.0.6
Release:        1
Summary:        Abstraction over xpyb
License:        WTFPL
Group:          Development/Languages/Python
URL:            https://github.com/BurntSushi/xpybutil
Source:         https://github.com/BurntSushi/xpybutil/archive/%{version}.tar.gz
Patch0:         python-xpybutil-0.0.5-remove-selftest.patch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-xcffib
BuildRequires:  python-rpm-macros
Requires:       python3-xcffib
BuildArch:      noarch

%description
xpybutil is an abstraction over the X Python Binding (xpyb). It exists
because xpyb is a very low level library that communicates with X.

%prep
%setup -q -n xpybutil-%{version}
%patch0 -p1

%build
%py3_build

%install
%py3_install

%files
%license COPYING
%doc README.md
%{python3_sitelib}/*

%changelog
* Thu Aug 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.6
- Rebuilt for Fedora
* Mon Jul 22 2019 mvetter@suse.com
- Update to 0.0.6:
  * Fixed bug affecting windows with opacity==0
- Refresh python-xpybutil-0.0.5-remove-selftest.patch
* Wed Jul 18 2018 tchvatal@suse.com
- Require python-rpm-macros
* Wed Jun  6 2018 mvetter@suse.com
- Add python-xpybutil-0.0.5-remove-selftest.patch:
  Don't test whether package itself is present
  Don't install README here too
* Wed Jun  6 2018 mvetter@suse.com
- Initial package in version 0.0.5 for openSUSE
