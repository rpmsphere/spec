%undefine _debugsource_packages
Name:		buc
Version:	0.5.2
Release:	1
Summary:	Parser xml in C accompanied by a dynamic generation of interfaces in C++ with QT
License:	GPLv2
URL:		http://buc.billeragroup.net/
Group:		Development/Tools
Source0:	%{name}-%{version}_src_full.tar.gz
Patch0:		%{name}-%{version}-gcc44.patch
BuildRequires:	qt4-devel

%description
BUC - Just A Click - ( an XML parser in C accompanied by a dynamic
generation of interfaces in C + + with QT ) is an Open Source Software
(GPL2) for GNU / Linux, developed by Matthew Avalle in collaboration with
Valerio Billera and SiciLinuX Group, able to transform bash script
(made executable text file containing commands to be executed) in
applications with graphical user interface and convenient to give a
graphical interface to programs that can be performed by the command line.

%prep
%setup -n zip -q
%patch0
sed -i '1i #include <unistd.h>' frmMain.cpp

%build
qmake-qt4 PREFIX=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT

# create /buc
%__install -d -m755 %{buildroot}%{_bindir}
%__install -d -m755 %{buildroot}%{_datadir}/%{name}

# binary
%__install -m755 %{name} %{buildroot}%{_datadir}/%{name}/%{name}
%__install -m755 bucd/usr/local/bin/%{name} %{buildroot}%{_bindir}
sed -i -e 's: #!/bin/bash:#!/bin/bash:' %{buildroot}%{_bindir}/%{name}
sed -i -e 's:dirname=/usr/local/buc/:dirname=/usr/share/buc/:' %{buildroot}%{_bindir}/%{name}

# datafiles
%__cp -a bucd/usr/local/%{name}/icon* %{buildroot}%{_datadir}/%{name}
%__install -dm755 %{buildroot}%{_datadir}/applications
%__install -Dm644 bucd/usr/share/icons/hicolor/48x48/apps/buc.png %{buildroot}%{_datadir}/pixmaps/buc.png
%__install -Dm644 bucd/usr/share/mime/packages/buc.xml %{buildroot}%{_datadir}/mime/packages/buc.xml

# desktopfile
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=BUC
GenericName=Dynamic Dialog Editor
Exec=%{name} %f
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
X-MultipleArgs=false
X-KDE-StartupNotify=true
MimeType=text/buc;
Categories=Application;Qt;KDE;Development;
EOF

%post
update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc bucd/usr/local/buc/LICENSE README-ita
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
* Fri Jan 01 2010 Alberto Altieri <alberto.altieri@gmail.com>
- New version/release for MIB (Mandriva Italia Backport) users
