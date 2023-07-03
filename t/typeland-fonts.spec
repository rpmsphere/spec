%define	font_dir	%{_datadir}/fonts/typeland

Name:           typeland-fonts
Summary:        TypeLand Typefaces
Version:        2010trial
Release:        1.1
License:        Trialware
Group:          User Interface/X
URL:            https://typeland.com/
Source0:	https://file.typeland.com/typeface/TpldKhangXiDict/TpldKhangXiDictTrial_1.023.zip
Source1:	https://file.typeland.com/typeface/TpldYiFengScripture/TpldYiFengScripture_1.003.zip
Source2:	https://file.typeland.com/typeface/TpldLehBienLehsho/TpldLehBienLehshoTrial_1.010.zip
BuildArch:      noarch

%description
TypeLand includes chinese fonts auto-traced by Digidea Lee.
* Khang Xi Dict Trial: 2000 Characters
* Yi Feng Scripture: 429 Characters
* Leh Bien Lehsho Trial: 2862 Characters

%prep
%setup -q -c -a 1 -a 2

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{font_dir}
install -m 644 *.otf $RPM_BUILD_ROOT%{font_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.pdf
%{font_dir}

%changelog
* Sun Jan 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2010
- Rebuilt for Fedora
