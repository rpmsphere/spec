Name: impress-templates-chtsai
License: Creative Commons License
Group: Applications/Productivity
Summary: Templates by chtsai for Impress 
Version: 2005
Release: 1
URL: http://technology.chtsai.org/impress/
Source: %{name}.zip
BuildArch: noarch
Requires: libreoffice-impress

%description
Some Impress templates by C.H. Tsai(蔡志浩).

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/template/zh-TW/presnt
cp *.otp $RPM_BUILD_ROOT%{_libdir}/libreoffice/share/template/zh-TW/presnt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/libreoffice/share/template/zh-TW/presnt/*.otp

%changelog
* Mon Mar 05 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2005
- Rebuilt for Fedora
