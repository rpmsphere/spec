%undefine _debugsource_packages

Name:       flashqard  
Summary:    An educational software to improve your learning process
Version:    0.15.0
Release:    19.1
License:    GPL v2 or later
Group:      Amusements/Teaching/Language
URL:        https://flashqard-project.org
Source:     %{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  cmake, gcc-c++, qt4-devel, qt-webkit-devel
Patch1:     desktop.diff

%description  
FlashQard is an educational software to improve your learning process.

It is designed to help you learn not only a new language but anything that can be learnt!
This aim is achieved by using the widely used method, called Leitner System, and the idea
of "different card types for different purposes".

Leitner System (proposed by Sebastian Leitner in the 1970s) is one the most efficient
methods for learning. Which allows you to focus on the most difficult flashcards and not
waste your time on what you have already learnt.
  
%prep
%setup -q
%patch 1
sed -i '1i #include <QApplication>' src/MimeData.h
sed -i '1i #include <QDir>' src/Utilities.cpp

%build
qmake-qt4
make
./flashqard-desktop.sh > flashqard.desktop

%install
%__rm -rf $RPM_BUILD_ROOT
install -Dm644 icons/%{name}_16x16.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm644 icons/%{name}_22x22.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
install -Dm644 icons/%{name}_32x32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm644 icons/%{name}_64x64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -Dm644 icons/%{name}_128x128.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -Dm644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a src/kgeography_data $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog 
* Sun May 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.15.0
- Rebuilt for Fedora
* Sun Sep 27 2009 Shahab <shahab@flashqard-project.org>
- Initial RPM  
