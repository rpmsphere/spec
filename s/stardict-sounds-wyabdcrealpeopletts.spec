Name:           stardict-sounds-wyabdcrealpeopletts
Summary:        Wyabdc RealPeople TTS audio collection of english words
Version:        2.1.0
Release:        1
License:        GPLv2+
Group:          Productivity/Office/Dictionary
URL:            http://code.google.com/p/stardict-3/
BuildArch:      noarch
Requires:       stardict, sox
Source0:        http://stardict-3.googlecode.com/files/WyabdcRealPeopleTTS.tar.bz2
Source1:        license.txt

%description
This package contains many wav files which can be used by StarDict to pronounce
english words. Files originally come from wyabdc, http://www.zhimajie.net,
thanks xiaozima.

%prep
%setup -q -n WyabdcRealPeopleTTS
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_datadir}/stardict/WyabdcRealPeopleTTS
cp -a ? %{buildroot}%{_datadir}/stardict/WyabdcRealPeopleTTS

%clean
%__rm -rf %buildroot

%files
%doc license.txt readme.txt README
%{_datadir}/stardict/WyabdcRealPeopleTTS

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuild for Fedora
* Thu Nov 11 2010 kirill.kirillov@gmail.com
- Initial build of Wyabdc RealPeople TTS 2.1.0 sounds using spec
  by Lars Vogdt
