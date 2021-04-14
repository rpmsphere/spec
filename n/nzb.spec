%undefine _debugsource_packages

Name:			nzb
Version:		0.3
Summary:		A binary news grabber
License:		GPL
URL:			http://www.nzb.fi/
Group:			Productivity/Network/News/Utilities
Release:		23.1
Source:			http://sourceforge.net/projects/nzb/files/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	gcc-c++
BuildRequires:	qt4-devel

%description
nzb is a binary news grabber. It natively downloads, decodes and even streams
the files specified in the .nzb file, an XML format which describes binary
files on Usenet by their message-id.

%prep
%setup -q

%build
%{_qt4_qmake} QMAKE_CXXFLAGS+=-Wno-narrowing
%{__make} %{?jobs:-j%jobs}

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 755 src/nzb $RPM_BUILD_ROOT%{_bindir}
install -m 644 images/*.png $RPM_BUILD_ROOT%{_datadir}/pixmaps

cat <<_EOF_ >%{name}.desktop
[Desktop Entry]
Name=%{name}
GenericName=A binary news grabber
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=0
Categories=Network;News;
_EOF_

install -D -m 644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
desktop-file-install                                    \
 --delete-original                                      \
 --vendor ""                                            \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
 --add-category Network                                 \
 --add-category News                                    \
 $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*
%{_bindir}/%{name}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Mon Dec 01 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Mon Jun 15 2009 David Bolt <davjam@davjam.org> 0.1.9
- Upgraded to latest version
* Fri May  8 2009 David Bolt <davjam@davjam.org> 0.1.8
- First built for openSUSE
