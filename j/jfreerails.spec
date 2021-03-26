%define _cvs_build		1
%define _cvs_version	cvs20061028

Name:				jfreerails
Summary:			Freerails is a real time multi player strategy game
URL:				http://freerails.sourceforge.net/
Group:				Amusements/Games/Strategy/Turn Based
Version:			0.2.7
Release:			1
License:			GPL
BuildRequires:	ant
BuildRequires:	ImageMagick
BuildRequires:	java-1.8.0-openjdk-devel
Requires:			java >= 1.5
Requires:			jpackage-utils >= 1.5
Requires:			liquidlnf
Source0:			%{name}-%{version}.tar.bz2
BuildArch:		noarch

%description
Freerails is a real time multi player strategy game where players compete to
build the most powerful railroad empire. It is written in java.

%package manual
Summary:	User documentation for jfreerails
Group:		Documentation/Other

%description manual
User documentation for jfreerails.

%prep
%setup -q -n %{name}

%build
export LANG=de_DE
%ant

%install
%__rm -rf %{buildroot}
# jars
%__install -dm 755 %{buildroot}%{_javadir}
%__install -m 644 dist/lib/%{name}*.jar \
	%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# data files
%__install -dm 755 %{buildroot}%{_datadir}/%{name}
%__install -m 644 logging.properties \
	%{buildroot}%{_datadir}/%{name}

# startscript
%__cat > %{name} << EOF
#!/bin/sh
# source the jpackage helpers
VERBOSE=1
. %{_javadir}-utils/java-functions

# set JAVA_* environment variables
set_javacmd
check_java_env
set_jvm_dirs
set_options "-Djava.util.logging.config.file=%{_datadir}/%{name}/logging.properties"

CLASSPATH=\`build-classpath liquidlnf %{name}\`
MAIN_CLASS="%{name}.launcher.Launcher"

run
EOF
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name}* \
	%{buildroot}%{_bindir}

# icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
convert www/FreeRails.png -resize 48x48! \
	%{name}.png
%__install -m 644 %{name}.png \
	%{buildroot}%{_datadir}/pixmaps

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Name[zh_TW]=鐵道大亨
Comment=Freerails is a real time multi player strategy game
Comment[zh_TW]=Freerails 是一套即時多人遊戲，可以共同上網遊戲，也可以單機操作。
Type=Application
Terminal=false
Exec=%{name}
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;StrategyGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%doc ChangeLog README ReleaseNotes
%{_bindir}/%{name}
%{_javadir}/*.jar
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.png

%files manual
%doc spec/*

%changelog
* Fri Mar 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.7
- Rebuild for Fedora
* Tue Jan 13 2009 Feather Mountain <john@ossii.com.tw> - 0.2.7-0.cvs20061028.ossii
- Rebuild for M6(OSSII)
* Sat Oct 28 2006 Toni Graffy <toni@links2linux.de> - 0.2.7-0.pm.cvs20061028
- First packaged release 0.2.7
