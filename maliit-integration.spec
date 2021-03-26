Name:           maliit-integration
Version:        0.1
Release:        1.1
Summary:        Maliit integration support
License:        GPLv3
URL:            http://www.maliit.org
Source0:        %{name}-%{version}.tar.bz2
Requires:	maliit-framework
Requires:	meego-inputmethodbridges
Requires(post):   %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives
BuildArch:	noarch
%define _xinputconf %{_sysconfdir}/X11/xinit/xinput.d/maliit.conf

%description
Maliit integration support.

%prep
%setup -q

%post
%{_sbindir}/alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_xinputconf} 100 || :

%postun
if [ "$1" = "0" ]; then
  %{_sbindir}/alternatives --remove xinputrc %{_xinputconf} || :
  # if alternative was set to manual, reset to auto
  [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && %{_sbindir}/alternatives --auto xinputrc || :
fi

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README

%defattr(-,root,root,-)
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit/xinput.d
%{_sysconfdir}/X11/xinit/xinput.d/maliit.conf
%{_sysconfdir}/xdg/autostart/meego-im-uiserver.desktop
%{_bindir}/start-meego-im-uiserver

%defattr(-,root,root,-)
%{_sysconfdir}/xbindkeys.conf
%{_sysconfdir}/xdg/autostart/xbindkeys.desktop
%{_bindir}/rotate-screen
%dir %{_datadir}/meegotouch
%dir %{_datadir}/meegotouch/targets
%{_datadir}/meegotouch/targets/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for OSSII
