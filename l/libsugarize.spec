%undefine _debugsource_packages

Name:           libsugarize
Summary:        Preload library for sugarizing
Version:        2007
Release:        1
License:        LGPLv2
URL:		http://dev.laptop.org/git/users/albert/sugarize/
Source:         http://dev.laptop.org/git/users/albert/sugarize/snapshot/sugarize-master.tar.gz
Group:          Sugar/Libraries
BuildRequires:  libX11-devel
Requires:       sugar

%description
This wrapper makes any normal single-window X program sugar-compatible.

%prep
%setup -q -n sugarize-master

%build
cd xlogo.activity
gcc -s -W -Wall -Os -shared -fpic -Wl,-soname,libsugarize.so -Wl,-z,initfirst -nostartfiles -o libsugarize.so libsugarize.c -lX11 -ldl -lc

%install
rm -rf %{buildroot}
install -Dm755 xlogo.activity/libsugarize.so %{buildroot}/usr/libexec/libsugarize.so

%clean
rm -rf %{buildroot}

%files
%doc README
/usr/libexec/libsugarize.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2007
- Rebuilt for Fedora
