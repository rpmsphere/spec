Name:           oxim-panels-oxvkb
Version:        0.3
Release:        2
Summary:        Virtual Screen Keyboard For OXIM

Group:          User Interface/Desktops
License:        Commercial
URL:            none
Source0:        keyboard-600.conf
Source1:        keyboard-800.conf
Source2:        keyboard-600.xpm
Source3:        keyboard-800.xpm
#Source4:        oxvkb.sh
#Source5:        oxvkb.sysconfig
Source5:        oxvkb.conf
Source6:        keyboard-600.png
Source7:        keyboard-800.png
#Source8:        oxvkb.png
Source9:        keyboard-1024.xpm
Source10:       keyboard-768.xpm
Source11:       keyboard-1024.conf
Source12:       keyboard-768.conf
BuildArch:	noarch

Requires:       oxim >= 1.5.2

%description


%prep


%build

%install
rm -rf $RPM_BUILD_ROOT

# install oxvkb.sysconfig
#mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig
#install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/oxvkb

# install oxvkb.sh
#mkdir -p $RPM_BUILD_ROOT/%{_bindir}
#install -m 755 %{SOURCE4} $RPM_BUILD_ROOT/%{_bindir}/oxvkb

# install picture and config files.
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels

install -m 644 %{SOURCE9} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE10} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE11} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels
install -m 644 %{SOURCE12} $RPM_BUILD_ROOT/%{_libdir}/oxim/panels

%{__ln_s} keyboard-1024.conf $RPM_BUILD_ROOT/%{_libdir}/oxim/panels/keyboard.conf
%{__ln_s} keyboard-1024.xpm $RPM_BUILD_ROOT/%{_libdir}/oxim/panels/keyboard.xpm

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_libdir}/oxim/panels/*

%post
%{__cat} > %{_sysconfdir}/oxim/panel.conf << EOF
VIRTUAL_KEYBOARD=keyboard
AUTO_DOCK=no
EOF


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Wed Aug 10 2011 Wind <yc.yan@ossii.com.tw> - 0.3-2
- Much more updates.

* Mon Aug  8 2011 Wind <yc.yan@ossii.com.tw> - 0.3-1
- Much more updates.

* Thu Jul 21 2011 Wind <yc.yan@ossii.com.tw> - 0.2-2
- oxvkb -> oxim-panels-oxvkb.

* Tue Jul  5 2011 Wind <yc.yan@ossii.com.tw> - 0.2-1
- Add 1024, 768 resolution.

* Sun Jan 16 2011 Firefly <firefly@opendesktop.org.tw> - 0.1
- New Package.
