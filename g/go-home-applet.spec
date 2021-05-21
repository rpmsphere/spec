%define         schema_name go-home
Name:           go-home-applet
Version:        0.1
Release:        9
Summary:        Go home applet for GNOME
Group:          User Interface/Desktops
License:        GPL
URL:            https://launchpad.net/netbook-remix
Source0:        go-home-applet_0.1ubuntu9.tar.gz
BuildRequires:  intltool, gettext, pkgconfig
BuildRequires:  GConf2-devel, libgnomeui-devel, libwnck-devel, gnome-panel-devel
Requires:       GConf2, libgnomeui, libwnck, gnome-panel

%description
Shows the desktop.

%prep
%setup -q -n go-home-applet-0.1ubuntu9

%build
./autogen.sh
%configure
sed -i -e 's|-lglib-2.0|-lglib-2.0 -lgio-2.0 -lgnomeui-2|' -e 's|-I/usr/include/libgnome-2.0|-I/usr/include/libgnome-2.0 -I/usr/include/libgnomeui-2.0|' src/Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/go-home-applet

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Jun 9 2008 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1-9.ossii
- Initial package
