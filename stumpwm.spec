Name: stumpwm
Summary: The Stump Window Manager
Version: 19.11
Release: 1
Group: User Interface/X
License: GPL-2.0
URL: https://github.com/stumpwm/stumpwm
Source0: https://github.com/stumpwm/stumpwm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: sbcl
BuildRequires: cl-clx
BuildRequires: cl-ppcre
BuildRequires: cl-alexandria
Obsoletes: dswm

%description
StumpWM is a window manager written entirely in Common Lisp. It attempts to
be highly customizable while relying entirely on the keyboard for input.
You will not find buttons, icons, title bars, tool bars, or any of the other
conventional GUI widgets.

%prep
%setup -q
#mkdir -p $HOME/.dswm.d/rules.d
#sed -i '345i @item C-t g' dswm.texi.in

%build
./autogen.sh
%configure
make

%install
#sed -i 's|/usr/share/xsessions/|$(destdir)/usr/share/xsessions/|g' Makefile
#mkdir -p %{buildroot}/usr/share/xsessions
make install destdir=%{buildroot}

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%exclude %{_datadir}/info/dir
%{_datadir}/info/%{name}.info.*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}
/etc/dss/%{name}

%changelog
* Mon Dec 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 19.11
- Rebuild for Fedora
