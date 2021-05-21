Name:       retext
Version:	5.0.1
Release:	4.1
License:	GPL-3.0+
Summary:	Text editor for Markdown and reStructuredText
URL:		http://sourceforge.net/p/retext/home/ReText
Group:		Productivity/Editors/Other
Source:		http://sourceforge.net/projects/retext/files/ReText-5.0/ReText-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:  libpng-devel
BuildRequires:	desktop-file-utils
BuildRequires:	librsvg2-devel
BuildRequires:	librsvg2-tools
Requires:	python3-PyQt4
Requires:	python3-markdown
Requires:	python3-docutils
Requires:	python3-markups
BuildArch:	noarch

%description
ReText is a simple but powerful text editor for Markdown and reStructuredText.

%prep
%setup -q -n ReText-%{version}

%build

%install
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/%{name}/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/applications/

%{__cp} -r * $RPM_BUILD_ROOT%{_datadir}/%{name}/
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/LICENSE_GPL
%{__cp} -r icons/*.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/
ICONSIZE="16 22 32 48 64 128 256"
pushd $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
for i in $ICONSIZE; do
  mkdir -pv ${i}x${i}/apps/
  rsvg-convert -h $i -w $i scalable/apps/%{name}.svg -o ${i}x${i}/apps/%{name}.png
done
popd
ln -sf %{_datadir}/%{name}/retext.py $RPM_BUILD_ROOT%{_bindir}/retext
%{__cp} -r %{S:1} $RPM_BUILD_ROOT%{_datadir}/applications/

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Dec 18 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0.1
- Rebuilt for Fedora
* Sat Feb 18 2012 i@marguerite.su
- update to 3.0beta1
* Thu Dec 29 2011 i@marguerite.su
- initial package 2.1.3
