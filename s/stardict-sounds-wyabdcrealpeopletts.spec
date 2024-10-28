Name:           stardict-sounds-wyabdcrealpeopletts
Summary:        Wyabdc RealPeople TTS audio collection of english words
Version:        2.1.0
Release:        1
License:        GPLv2+
Group:          Productivity/Office/Dictionary
URL:            https://code.google.com/p/stardict-3/
BuildArch:      noarch
Requires:       stardict, sox
Source0:        https://stardict-3.googlecode.com/files/WyabdcRealPeopleTTS.tar.bz2
Source1:        %name.license.txt

%description
This package contains many wav files which can be used by StarDict to pronounce
english words. Files originally come from wyabdc, https://www.zhimajie.net,
thanks xiaozima.

%prep
%setup -q -n WyabdcRealPeopleTTS
cp %{SOURCE1} license.txt

%build

%install
mkdir -p %{buildroot}%{_datadir}/stardict/WyabdcRealPeopleTTS
cp -a ? %{buildroot}%{_datadir}/stardict/WyabdcRealPeopleTTS

%files
%doc license.txt readme.txt README
%{_datadir}/stardict/WyabdcRealPeopleTTS

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Thu Nov 11 2010 kirill.kirillov@gmail.com
- Initial build of Wyabdc RealPeople TTS 2.1.0 sounds using spec
  by Lars Vogdt
