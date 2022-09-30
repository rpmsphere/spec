Name:          kojo
Summary:       A Scala Learning Environment
URL:           http://www.kogics.net/kojo
Group:         Applications/Education
License:       GPL
Version:       2.9.23
Release:       1.bin
Source0:       https://github.com/litan/kojo/releases/download/2.9.23_release/Kojo_2_9_23.zip
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
%setup -q -n Kojo-z

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a * %{buildroot}%{_datadir}/%{name}

# script
mkdir -p %{buildroot}%{_bindir}
ln -s ../share/%{name}/bin/kojo %{buildroot}%{_bindir}/%{name}
cd %{buildroot}%{_datadir}/%{name}
sed -i 's|$0|$(realpath $0)|' bin/kojo
rm -rf bin/kojo.*

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
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9.23
- Initial binary package
