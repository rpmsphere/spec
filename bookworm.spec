Name:		bookworm
Version:	1.1.1
Release:	1
Summary:	A simple E-book reader
License:	GPLv3+
Group:		Office/Utilities
URL:		https://babluboy.github.io/bookworm
Source:		https://github.com/babluboy/bookworm/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	ImageMagick
BuildRequires:	vala
BuildRequires:	pkgconfig(gee-0.8)
BuildRequires:	pkgconfig(granite)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(sqlite3) >= 3.5.9
BuildRequires:	pkgconfig(webkit2gtk-4.0) >= 2.16.0
# Check list of dependencies
BuildRequires:	python3-html2text
BuildRequires:	poppler
Requires:	contractor
Requires:	python3-html2text
Requires:	poppler
Recommends:	unrar
Recommends:	unzip

%description
An eBook reader for Elementary OS.
It uses poppler for decoding and read formats like EPUB, PDF, mobi, cbr, etc.

%prep
%setup -q
chmod -x AUTHORS

%build
%cmake -DGSETTINGS_COMPILE=OFF
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/com.github.babluboy.%{name} %{buildroot}%{_bindir}/%{name}
# remove executable flags
find %{buildroot} -name \*.txt -exec chmod 0644 {} +
%find_lang com.github.babluboy.bookworm && cat com.github.babluboy.bookworm.lang >> %{name}.lang

%files -f %{name}.lang
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_datadir}/applications/com.github.babluboy.%{name}.desktop
%{_datadir}/glib-2.0/schemas/com.github.babluboy.%{name}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*%{name}*.??g
%{_datadir}/metainfo/com.github.babluboy.%{name}.appdata.xml
%{_datadir}/%{name}
%{_datadir}/contractor/com.github.babluboy.%{name}.contract

%changelog
* Mon Apr 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuild for Fedora
* Sat Feb 02 2019 daviddavid <daviddavid> 1.1.1-1.mga7
+ Revision: 1362383
- initial package bookworm
