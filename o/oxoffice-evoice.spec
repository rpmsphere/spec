%define extension_dir /opt/oxoffice3/share/extension/install/
%define extension_name EVoice

Name:		oxoffice-evoice
Version:	1.0.0
Release:	1
Summary:	Support for add voice in Impress documents
Group:		Applications/Productivity
License:	opensource
URL:		http://extensions.openoffice.org/en/project/eVoice
Source0:	http://nchc.dl.sourceforge.net/project/aoo-extensions/545/1/EVoice.oxt
BuildArch:	noarch
Requires:	oxoffice
BuildRequires: 	oxoffice

%description
eVoice is an easy-to-use extension to embed voice comments in your slides.
It provides the capabilities of recording and adding audio commentaries to
your slide shows. Every comment will be associated with a single slide and
embedded inside the Impress document in Speex format to keep file size small.
Comments will also be automatically reproduced during presentation.

%prep
%setup -T -c
unzip %{SOURCE0}
sed -i '/<simple-license/,/<\/simple-license/d' description.xml
zip -r %{extension_name}.oxt *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{extension_dir}
cp -a %{extension_name}.oxt $RPM_BUILD_ROOT/%{extension_dir}

%post
/usr/bin/unopkg add --shared --force %{extension_dir}/%{extension_name}.oxt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{extension_dir}/%{extension_name}.oxt

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Mon May 7 2012 Wei-Lun Chao <bluebat@member.fsf.org>
- Update to 1.0.0

* Mon May 7 2012 Eric Lee <eric.lee@ossii.com.tw> 
- Initial package for OSSII
