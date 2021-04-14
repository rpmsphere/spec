Name: xirod-fonts
Summary: Free xirod fonts by Larabie
Version: 3.001
Release: 2.1
License: free commercial
Group: System/X11/Fonts
Source0: xirod.zip
URL: http://typodermicfonts.com/xirod/
BuildArch: noarch

%description
Xirod is a square, sci-fi techno headline font. In OpenType savvy applications,
letters change in order to harmonize with adjacent letters. Strange alternate
letters can be accessed using the OpenType “Stylistic Alternates” feature.

%prep
%setup -q -c

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/xirod
cp *.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/xirod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc *.html *.pdf
%{_datadir}/fonts/xirod

%changelog
* Tue Jul 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.001
- Rebuilt for Fedora
* Thu Jan 01 2009 - Mathias Homann <admin@eregion.de>
- import into build tree
