Summary: A simple but powerful Java IDE
Name: greenfoot
Version: 3.0.2
Release: 1.bin
License: GPL
Group: Development
URL: http://www.greenfoot.org/
Source0: http://www.greenfoot.org/download/files/Greenfoot-linux-302.deb
#Source1: http://www.westart.tw/greenfoot/?q=file/download/55
Source1: %{name}-zht.zip
BuildArch: noarch
Requires: java-devel-openjdk
Requires: javafx

%description
Greenfoot teaches object orientation with Java. Create 'actors' which live
in 'worlds' to build games, simulations, and other graphical programs.
Greenfoot is visual and interactive. Visualisation and interaction tools
are built into the environment. The actors are programmed in standard textual
Java code, providing a combination of programming experience in a traditional
text-based language with visual execution.

%prep
%setup -q -T -c -a 1
ar -x %{SOURCE0}

%build

%install
mkdir -p $RPM_BUILD_ROOT
tar xf data.tar.?z -C $RPM_BUILD_ROOT
sed -i 's|java-.-openjdk|java-openjdk|' $RPM_BUILD_ROOT%{_bindir}/%{name}
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}
mv chinese_traditional $RPM_BUILD_ROOT%{_datadir}/%{name}/chinese_t
sed -i '58i bluej.language19=chinese_t:Chinese_T' $RPM_BUILD_ROOT%{_datadir}/%{name}/bluej.defs

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/Greenfoot
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Thu Dec 31 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.2
- Initial binary package
