Name: basic256
Version: 1.1.4.0
Release: 9.4
URL: http://kidbasic.sourceforge.net
Source: http://sourceforge.net/projects/kidbasic/files/basic256/%{name}_%{version}.orig.tar.gz
Source1: basic256.desktop
Source2: basic256_32.png
License: GPL
Group: Development/Other
BuildRequires: libpng-devel espeak-devel
BuildRequires: qt5-qtbase-devel qt5-qtwebkit-devel qt5-qtserialport-devel qt5-qtmultimedia-devel
BuildRequires: SDL-devel SDL_mixer-devel sqlite-devel gcc-c++ flex bison
Summary: Simple BASIC IDE

%description
BASIC-256 allows young children to learn to program. 
It was written in response to David Brin's article, "Why Johnny Can't Code," 
in which he bemoans the lack of a simple, line-oriented programming language 
for children that runs on modern computers. It features a byte-code compiler 
and interpreter, a debugger, easy to use graphical and text output, and an editor.

%prep
%setup -q

%build
qmake-qt5 BASIC256.pro
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_datadir/%{name}/Examples
mkdir -p $RPM_BUILD_ROOT%_datadir/%{name}/help
install -Dm755 %{name} $RPM_BUILD_ROOT%_bindir/%{name}
install Translations/*.qm $RPM_BUILD_ROOT%_datadir/%{name}
install -D %SOURCE1 $RPM_BUILD_ROOT%_datadir/applications/%{name}.desktop
install -D %SOURCE2 $RPM_BUILD_ROOT%_datadir/pixmaps/%{name}.png
cp -r Examples $RPM_BUILD_ROOT%_datadir/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CONTRIBUTORS license.txt ChangeLog
%{_bindir}/*
%{_datadir}/%name
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/%name.png

%changelog
* Wed Dec 31 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4.0
- Rebuild for Fedora
* Wed Jan 26 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.6-1mdv2010.1
+ Revision: 632933
+ rebuild (emptylog)
* Sat Jan 22 2011 Александр Казанцев <kazancas@mandriva.org> 0.9.6-1
+ Revision: 632372
- initial release for Mandriva
- import basic256
* Sat Jan 22 2010 Alexander Kazancev <kazancas@mandriva.ru> - 0.9.6-1mdv
- Initial release for Mandriva
