Summary:	A command line tool for moving a MP3 file
Name:		mp3tool
Version:	0.3.1
Release:	4.1
URL:		https://wpitchoune.net/blog/mp3tool/
License:	GNU General Public License version 2
Group:		Applications/Multimedia
Source0:	https://wpitchoune.net/mp3tool/files/%{name}-%{version}.tar.gz

%description
The MP3 files contain information about the name of the artist, the name
of the album, the sound title, etc.

MP3Tool is a command line tool for moving a MP3 file according to these
information. It can also output the information.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.*

%changelog
* Fri May 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
