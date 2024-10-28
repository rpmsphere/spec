%define fontdir %{_datadir}/fonts/cjkfonts-sil

Name:           cjkfonts-sil-fonts
Version:        2024.3
Release:        1
Summary:        SIL Fonts from cjkfonts.io
License:        SIL OPEN FONT LICENSE
Group:          System/X11/Fonts
URL:            https://cjkfonts.io/
Source0:        https://cjkfonts.io/downloadfont?font_id=cjkfonts_001&v=1.11#/cjkfonts_allseto_v1.11.zip
Source1:        https://cjkfonts.io/downloadfont?font_id=cjkfonts_003&v=0.02#/ThePeakFontBeta_V0_101.zip
Source2:        https://cjkfonts.io/downloadfont?font_id=cjkfonts_002&v=1.00#/cjkfonts_handwriting4.zip
BuildArch:      noarch

%description
全瀨體 v1.11：基於瀨戶字體透過深度學習智能造字，支持繁中、簡中、日及韓，免費可商業用途。
隨峰體 v0.02：逐字逐字以啫喱筆寫成的手寫字體，而且保留手寫痕跡和瑕疵。
手寫4 v1.00：基於清松手寫體4透過深度學習智能造字， 免費可商業用途。

%prep
%setup -q -c
mv license.txt allseto.license
unzip %{SOURCE1}
mv license.txt thepeak.license
unzip %{SOURCE2}
mv license.txt handwriting4.license

%build

%install
install -d %{buildroot}%{fontdir}
install -m644 *.ttf %{buildroot}%{fontdir}

%files
%doc *.license
%{fontdir}/*

%changelog
* Sun Mar 17 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2024.3
- Rebuilt for Fedora
