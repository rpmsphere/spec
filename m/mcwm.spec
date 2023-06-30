Name:           mcwm
Version:        20130209
Release:        5.1
Summary:        MC's Window Manager
Group:          User Interface/Desktops
License:        ISC
URL:            https://hack.org/mc/hacks/mcwm
Source0:        https://hack.org/mc/hacks/mcwm/%{name}-%{version}-2.tar.bz2
Source1:        mcwm.desktop
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-wm-devel

%description
mcwm is a minimalist floating window manager for the X Window System
written directly on top of the X protocol C-language Binding, XCB.
In mcwm all functions are available from the keyboard but a pointing device
can be used for move, resize and raise/lower.

%prep
%setup -q -n %{name}-%{version}-2

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 mcwm $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 0644 mcwm.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -Dm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/mcwm.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE
%{_bindir}/mcwm
%{_mandir}/man1/mcwm.1.*
%{_datadir}/xsessions/mcwm.desktop

%changelog
* Wed Apr 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 20130209-2
- Rebuilt for Fedora
* Tue Feb 28 2012 Damien Durand <splinux25@gmail.com> - 20111124-1
- Initial release
