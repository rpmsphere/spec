Name: timgm6mb-soundfont
Summary: TimGM6mb SoundFont from MuseScore 1.3
Version: 1.3
Release: 2.1
Group: Applications/Multimedia
License: GPLv2
URL: https://ocmnet.com/saxguru/TimGM6mb.htm
Source0: https://http.debian.net/debian/pool/main/t/timgm6mb-soundfont/timgm6mb-soundfont_1.3.orig.tar.gz
BuildArch: noarch

%description
This is a small but complete GM SoundFont, originally packaged with
MuseScore 1.3, but dropped from MuseScore 2.0.

%prep
%setup -q -n timgm6mb-soundfont_1.3

%build

%install
install -Dm644 TimGM6mb.sf2 %{buildroot}%{_datadir}/soundfonts/TimGM6mb.sf2

%files
%{_datadir}/soundfonts/TimGM6mb.sf2

%changelog
* Tue Aug 22 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
