%undefine _debugsource_packages

Name:           lunzip
Summary:        Decompressor for lzip files
Version:        1.5
Release:        3.1
License:        GPLv3+
Group:          Archiving/Compression
URL:            https://www.nongnu.org/lzip/lunzip.html
Source0:        https://download.savannah.gnu.org/releases/lzip/%{name}-%{version}.tar.gz
BuildRequires:  lzip

%description
Lunzip is a decompressor for lzip files. It is written in C and its small size
makes it well suited for embedded devices or software installers that need
to decompress files but do not need compression capabilities.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%files
%{_bindir}/lunzip
%{_mandir}/man1/lunzip.1*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Wed Feb 18 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.1-1
+ Revision: 789134
- update to 1.1
- run make check after build
* Tue Mar 13 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.0-1
+ Revision: 784552
- imported package lunzip
