Name:           galaxium
Version:        0.7.4.2
Release:        0.3199
License:        GNU General Public License (GPL)
URL:            http://code.google.com/p/galaxium/
Group:          Networking/Talk
Summary:        Multi-Protocol Instant Messenger
Source:         %{name}_%{version}.tar.gz
BuildRequires:  mono-devel mono-addins-devel mono-data-sqlite
BuildRequires:  gtk-sharp2-devel gecko-sharp2-devel notify-sharp-devel gnome-sharp-devel
BuildRequires:  libanculus-sharp-devel gcc intltool ndesk-dbus-devel ndesk-dbus-glib-devel gstreamer-devel

%description
Galaxium Messenger: An instant messenger application which currently
allows users to connect to the MSN, IRC, Jabber and GoogleTalk services.
It is cross platform and uses the Mono framework and GTK# for the user
interface.

%prep
%setup -q

%build
sh autogen.sh --prefix=%{_prefix} --disable-webkit
make  

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
echo -e 'Name[zh_TW]=銀河即時通\nComment[zh_TW]=Galaxium 支援多種協定的即時通程式' >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_prefix}/lib/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/man/man1/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_prefix}/lib/pkgconfig/%{name}-*.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Apr 23 2009 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Thu Sep 04 2008 Ben Motmans <ben.motmans@gmail.com>
- Initial package for OpenSUSE
