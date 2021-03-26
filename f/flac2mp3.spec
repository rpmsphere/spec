Name:           flac2mp3
Version:        0.3.0.RC1
Release:        3.1
License:        GPL
Group:          Multimedia/Audio
Summary:        Convert flac file to mp3
Requires:	perl-Text-Glob perl-Audio-FLAC-Header perl-File-Which perl-File-Find-Rule 
Requires:	perl-MP3-Tag perl-Number-Compare lame flac
Source:		http://robinbowes.com/download/flac2mp3/%{name}-%{version}.tar.bz2
BuildArch:  noarch

%description
Perl script to convert flac files to mp3.

%prep
%setup -q

%build
%{__rm} -rf lib

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D  -m 0755 flac2mp3.pl  $RPM_BUILD_ROOT%{_bindir}/flac2mp3.pl

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc readme.txt changelog.txt
%{_bindir}/flac2mp3.pl

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0RC1
- Rebuild for Fedora
* Fri Jan 11 2008 crrodriguez@suse.de
- initial build as package
