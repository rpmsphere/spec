Name:          kojo
Summary:       A Scala Learning Environment
URL:           http://www.kogics.net/kojo
Group:         Applications/Education
License:       GPL
Version:       2.4.08
Release:       1.bin
Source0:       https://bitbucket.org/lalit_pant/kojo/downloads/kojoInstall-%{version}.jar
Source1:       http://kogics.wdfiles.com/local--files/kojo-silent-install/auto-install.xml
BuildRequires: java-openjdk
Requires:      jre
BuildArch:     noarch

%description
With many different features that enable play, exploration, discovery,
creation, and learning in the areas of:
* Computer Programming and Computational thinking
* Math and Science
* Inductive, Deductive, Systematic, and Analytical thinking
* Art, Music, and Creative thinking
* Problem Solving strategies
* Electronics and Robotics
* Computer and Internet literacy

%prep
%setup -T -c
cp %{SOURCE0} %{SOURCE1} .
sed -i 's|/home/lalit/Kojo2.auto|%{buildroot}%{_datadir}/%{name}|' auto-install.xml

%build
#ant

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
java -jar kojoInstall-%{version}.jar auto-install.xml

# script
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_datadir}/%{name}
sed -i 's|$0|$(realpath $0)|' bin/kojo
ln -s ../share/%{name}/bin/kojo %{buildroot}%{_bindir}/%{name}
rm -rf bin/kojo.exe Uninstaller ApplicationShortcuts .installationinformation

# freedesktop.org menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Kojo
Comment=A Scala Learning Environment
Exec=%{name}
Terminal=false
Type=Application
Icon=/usr/share/kojo/icons/kojo64.png
Encoding=UTF-8
Categories=Application;Education;Java;
EOF

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jan 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.08
- Initial binary package
