Name:           png2ico
Version:        2002.12.08
Release:        5.1
Summary:        PNG to icon converter
Source:         %{name}-src-2002-12-08.tar.bz2
URL:            http://www.winterdrache.de/freeware/png2ico/
Group:          Productivity/Graphics/Other
License:        OSI Approved
BuildRoot:      %{_tmppath}/build-%{name}-%{version}
BuildRequires:  make libpng-devel gcc-c++

%description
Converts PNG files to Windows icon resource files. If you're looking for a program
to create a favicon.ico for your website, look no further. If you need instructions
or don't even know what a favicon is, check out my short tutorial on how to create
and install a favicon.ico.

The program is extremely simple to use. To create a favicon.ico that contains a
logo in the resolutions 16x16 and 32x32 (an icon can contain multiple images of
different sizes, but a single 16x16 image is enough for a favicon), you would use
a command like the following:
     png2ico favicon.ico logo16x16.png logo32x32.png

%prep
%setup -q -n png2ico
sed -i '1i #include <cstring>' png2ico.cpp

%build
make

%install
%__install -m 755 -d ${RPM_BUILD_ROOT}%{_bindir}
%__install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/
%__install -m 755 -d ${RPM_BUILD_ROOT}%{_mandir}/man1/
gzip doc/%{name}.1
%__install -m 0644 doc/%{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc LICENSE README VERSION README.unix
%{_bindir}/*
%{_mandir}/man1/%{name}.1.gz

%changelog
* Tue Dec 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2002.12.08
- Rebuilt for Fedora
* Thu Oct 27 2009 Dirk Stöcker <opensuse@dstoecker.de> 2002.12.08
- created
