Summary: 	Linux enhanced port of Winpopup
Name: 		linpopup
Version: 	2.1.0
Release:	10.1
License:	GPL
Group: 		Networking/Chat
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}.png
BuildRequires:  libpng-devel
BuildRequires:	gtk2-devel libXmu-devel
Requires:	gtk2 libXmu
Requires:	samba-client samba-common
URL: 		http://linpopup2.sourceforge.net

%description
Xwindow graphical port of Winpopup, running over Samba.
Permits to communicate with a windows computer that runs Winpopup,
sending or receiving message. Also provides an alternative way
to communicate between Linux computers that run Samba.

%prep
%setup -q

%build
export LDFLAGS+=" -lX11 -Wl,--allow-multiple-definition"
%{configure} --prefix=%{_prefix}
%{__make} %{?_smp_mflags} %{?mflags} CFLAGS+=" -Wno-format-security"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{?mflags_install} DESTDIR=$RPM_BUILD_ROOT install

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
cat >$RPM_BUILD_ROOT%{_datadir}/applications/%name.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=LinPopUp
Comment=Linux enhanced port of Winpopup
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Network;IRCClient;GTK;
EOF

# icon
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__install -m 644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%post

echo "*IMPORTANT*"
echo "-----------"
echo "You will need to edit the file /etc/samba/smb.conf"
echo "(as root) and add the following message command"
echo "to the [global] section:"
echo
echo 'message command = %{_bindir}/linpopup "%f" "%m" %s'
echo
echo "See the file %{_defaultdocdir}/%{name}-%{version}/INSTALL"
echo "for more detailed information."

%postun

[ -d "%{_localstatedir}/linpopup" ] && rm -rf "%{_localstatedir}/linpopup" || true
[ -d "%{_datadir}/linpopup" ] && rm -rf "%{_datadir}/linpopup" || true

echo "*IMPORTANT*"
echo "-----------"
echo "You will need to edit the file /etc/samba/smb.conf"
echo "(as root) and comment out the message command"
echo "in the [global] section:"
echo
echo '# message command = /usr/bin/linpopup "%f" "%m" %s'

%files
%{_bindir}/LinPopUp
%{_bindir}/linpopup
%{_datadir}/linpopup/gtkrc
%{_datadir}/linpopup/pixmaps/linpopup_tray.xpm
%{_datadir}/linpopup/pixmaps/little_igloo.xpm
%{_datadir}/locale/de/LC_MESSAGES/linpopup.mo
%{_datadir}/locale/fr/LC_MESSAGES/linpopup.mo
%{_datadir}/locale/nl/LC_MESSAGES/linpopup.mo
%{_datadir}/locale/ru/LC_MESSAGES/linpopup.mo
%{_mandir}/man1/LinPopUp.1.gz
%{_mandir}/man1/linpopup.1.gz
%{_localstatedir}/linpopup/messages.dat
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS TODO

%changelog
* Thu Nov 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuild for Fedora
* Sat Nov 3 2007 Stumpy842 <stump842@gmail.com> 2.1.0-3pclos_tinyme2007
- added update_desktop_database to post install
- added clean_desktop_database to post uninstall
- added post uninstall instructions
- changed occurences of %%{_var}/lib to %%{_localstatedir}
* Thu Oct 4 2007 Stumpy842 <stump842@gmail.com> 2.1.0-2pclos_tinyme2007
- added requires for samba-client and samba-server
- added post install instructions
* Sun Sep 30 2007 Stumpy842 <stump842@gmail.com> 2.1.0-1pclos_tinyme2007
- rebuild for pclos2007
