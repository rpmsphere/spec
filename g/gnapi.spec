Summary:		A NAPI-PROJEKT client
Name:			gnapi	
Version:		0.2.2
Release:		21.1
License:		GPL
Group:			Productivity/Multimedia/Other
Source0:		https://sourceforge.net/projects/gnapi/files/0.2/%{name}_%{version}.tar.gz
URL:			https://gnapi.sourceforge.net/
BuildRequires:  libpng-devel
BuildRequires:  libcurl-devel
BuildRequires:	libnotify-devel notification-daemon
BuildRequires:	openssl-devel
BuildRequires:	gtk2-devel gnome-vfs2-devel
BuildRequires:	libxml2-devel
BuildRequires:  sane-backends-libs
BuildRequires:  nautilus-devel libsoup-devel
Requires:		p7zip
BuildRequires:  compat-ffmpeg-devel
BuildRequires:  udisks2

%description
Download subtitles under Linux with just one click!

%package kde
Summary: A NAPI-PROJET client with support for KDE

%description kde
Download subtitles under Linux with just one click!

%prep
%setup -q
sed -i 's/-o root -g root//' Makefile
%ifarch x86_64 aarch64
sed -i 's|usr/lib|usr/lib64|' Makefile
%endif

%build
export CFLAGS="-I/usr/include/compat-ffmpeg -L%{_libdir}/compat-ffmpeg -ldl -lavcodec -Wl,--allow-multiple-definition"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
#sed -i 's|/usr/share/pixmaps/%{name}/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_libdir}/gnapi/plugins/libnapi.so
%{_libdir}/gnapi/plugins/libopensub.so
%{_libdir}/nautilus/extensions-2.0/libnautilus-gnapi.so
%{_datadir}/docs/gnapi/copyright
%{_datadir}/gnapi/info.glade
%{_datadir}/gnapi/napi_config.glade
%{_datadir}/gnapi/os.png
%{_datadir}/gnapi/os_config.glade
%{_datadir}/gnapi/scan.glade
%{_datadir}/locale/pl/LC_MESSAGES/gnapi.mo

%files kde
%{_datadir}/Thunar/sendto/gnapi-kde.desktop
%{_datadir}/apps/dolphin/servicemenus/gnapi-kde.desktop
%{_datadir}/apps/konqueror/servicemenus/gnapi-kde.desktop
%{_datadir}/kde4/services/ServiceMenus/gnapi-kde4.desktop

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
* Sat Apr 19 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.8-4
* Sun Feb 17 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.7
* Thu Feb 14 2008 Piotr Pacholak <obi.gts@gmail.com>
- initial 
