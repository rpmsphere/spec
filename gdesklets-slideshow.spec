Name:		gdesklets-slideshow
Version:	0.9
Release:	1
Summary:	A slideshow of collection for gdesklets
Group:		User Interface/Desktops
License:	GPLv2+
URL:		http://gdesklets.de/?q=desklet/view/221
Source0:	http://www.gdesklets.de/files/desklets/SlideShow/SlideShow-%{version}.tar.gz
Source1:	http://www.gdesklets.de/files/controls/ImageSlideShow/ImageSlideShow-0.8.tar.gz
BuildArch:	noarch

%define		_appname	SlideShow
%define		_ctrlname	ImageSlideShow

BuildRequires:	python2
Requires:	gdesklets
Requires:	python-imaging

%description
Cycle through a collection of pictures. Will display image captions
(IPTC,Jpeg Comment, EXIF) if available.

%prep
%setup -q -c %{name}-%{version} -a1

%build

%install
rm -rf $RPM_BUILD_ROOT
#need to install the control first
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/
install -p -m644 %{_ctrlname}/* $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/.
rm $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/MANIFEST
rm $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/README

#add shebang and execution mode
find $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/. \( -name "*.py" \) -exec sed -i '1i\#!/usr/bin/python' {} \;
find $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Controls/%{_ctrlname}/. \( -name "*.py" \) | xargs chmod a+x

#install the display now
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/%{_appname}/
cp -a %{_appname}/* $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/%{_appname}/.
rm $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/%{_appname}/LICENSE
rm $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/%{_appname}/todo

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_datadir}/gdesklets/Controls/ImageSlideShow/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{_appname}/LICENSE %{_appname}/todo %{_ctrlname}/MANIFEST %{_ctrlname}/README
%{_datadir}/gdesklets/Controls/ImageSlideShow/
%{_datadir}/gdesklets/Displays/SlideShow/

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuild for Fedora
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Feb 6 2009  Jonathan MERCIER <bioinfornatics-at-gmail.com> - 0.9-5
- change the name of rpm SlideShow to gdesklet-SlideShow
* Sat Jan 31 2009 Jonathan MERCIER <bioinfornatics-at-gmail.com> - 0.9-4
- Updated the summary in spec file
* Thu Jan 29 2009 Jonathan MERCIER <bioinfornatics-at-gmail.com> - 0.9-3
- Updated the spec file
* Wed Jan 21 2009 Jonathan MERCIER <bioinfornatics-at-gmail.com> - 0.9-2
- Updated the spec file
- Updated License
* Mon Jan 12 2009 Jonathan MERCIER <bioinfornatics-at-gmail.com> - 0.9-1
- Initial Packaging for Fedora
