Name:          lopster
Version:       1.2.2
Release:       10.1
Summary:       A Napster Client developed in C using the GTK user interface
Group:         Graphical Desktop/Applications/Networking
URL:           http://lopster.sourceforge.net
Source:        http://lopster.sourceforge.net/download/lopster-%{version}.tar.gz
Patch0:        lopster-log.patch
License:       GPL
BuildRequires: glibc-devel
BuildRequires: flac-devel
BuildRequires: glib-devel
BuildRequires: gtk+-devel
BuildRequires: libogg-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: zlib-devel

%description
Lopster is a Napster Client developed in C using the GTK user interface. 
Napster is a protocol for sharing MP3 files between users. 
With Napster, the files stay on the client machine, never passing through the server. 
The server provides the ability to search for particular files and initiate a direct transfer between the clients. 
In addition, chat forums similar to IRC are available.

%prep
%setup -q
%patch0 -p1
%build
%configure
make CFLAGS+=-Wno-format-security

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall

install -d $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/lopster.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Lopster
GenericName=Peer to Peer Client
GenericName[it]=Client p2p
Comment=Peer to Peer Client
Comment[it]=Lopster è un client p2p multipiattaforma scritto in C che supporta il protocollo OpenNap, evoluzione del protocollo Napster
Exec=lopster
Type=Application
Terminal=false
Icon=/usr/share/lopster/pixmaps/logo1.xpm
Categories=Application;Network; 
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/lopster
%{_datadir}/lopster
%{_datadir}/applications/lopster.desktop
%doc AUTHORS BUGS COPYING NEWS README TODO

%changelog
* Wed Jun 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
* Fri Aug 01 2008 Tiziana Ferro <tiziana.ferro@email.it> 1.2.2-5mamba
- rebuild with new libFLAC libraries
- update file desktop entry
- added patch for lvalue error using GCC4
- added buildrequirements
* Fri Jun 10 2005 Davide Madrisan <davide.madrisan@qilinux.it> 1.2.2-4qilnx
- rebuild with new libFLAC libraries
- added build requirements
* Mon Nov 15 2004 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 1.2.2-3qilnx
- modified lopster exec parameters in Exec field
* Mon Nov 15 2004 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 1.2.2-2qilnx
- added lopster icon
* Sat Nov 13 2004 Silvan Calarco <silvan.calarco@qilinux.it> 1.2.2-1qilnx
- update to version 1.2.2 by autospec
* Fri Jul 21 2003 Silvan Calarco <silvan.calarco@qinet.it> 1.2.0-1qilnx
- first build for lopster
