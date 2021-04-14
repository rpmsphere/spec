Name:			kenny-x
Version:		0.1
Summary:		A graphical kenny speak convertor
Group:			Productivity/Text/Convertors
License:		Freeware
Release:		52.1
Source:			%{name}-%{version}.tar.gz
Patch0:			%{name}-%{version}-imagepath.diff
URL:            	http://shang.de/d6/node/15
BuildArch:		noarch
Requires:		tk >= 8.4
BuildRequires:		desktop-file-utils
Requires:		hicolor-icon-theme
BuildRequires:		hicolor-icon-theme

%description
A graphical kenny speak convertor.

%prep
%setup -q
%patch0

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/%{name}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

install -m755 kenny.tcl $RPM_BUILD_ROOT/usr/lib/%{name}/
install -m644 *.gif $RPM_BUILD_ROOT/usr/lib/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -m 644 contrib/%{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m644 contrib/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

desktop-file-install                                    \
 --delete-original                                      \
 --vendor ""                                            \
 --dir $RPM_BUILD_ROOT%{_datadir}/applications          \
 --add-category Utility                                 \
 --add-category TextEditor                              \
 $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

%files
/usr/lib/%{name}
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%doc readme.txt

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Tue Jun 23 2009 David Bolt <davjam@davjam.org> 0.1
- Updated URL
