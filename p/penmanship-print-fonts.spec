%define	fontdir	%{_datadir}/fonts/penman

Summary: Free Manuscript Font
Name: penmanship-print-fonts
Version: 1998.08
Release: 2.1
License: freeware, no commercial
Group: User Interface/X
BuildArch: noarch
Source0: https://desktoppub.about.com/library/fonts/hs/penman.zip
URL: https://desktoppub.about.com/od/lessonplans/ig/Free-Print---Cursive-Fonts/Penmanship-Print.htm
Requires(post): fontconfig

%description
Ruled manuscript font has solid caps and baseline rules and dashed x-height
rule. Can't quite identify this style. It differs from the standards I've found
in several ways: thinner, J has top horizontal stroke, straight tail on q
(no hook), shorter ascenders and descenders, G includes an extra vertical stroke.
Yet still has a very school-like appearance.
Author: rchrdd@hotmail.com

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
install -Dm644 PENMP___.TTF %{buildroot}%{fontdir}/penmanship-print.ttf

%clean
rm -rf %{buildroot}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc Penprint.txt
%{fontdir}/*

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1998.08
- Rebuilt for Fedora
