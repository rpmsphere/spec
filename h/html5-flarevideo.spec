Summary: HTML5 & Flash Video Player
Name: html5-flarevideo
Version: 1.2
Release: 3
License: MIT
Group: Application/Multimedia
#Source0: https://nodeload.github.com/maccman/flarevideo/zipball/master
Source0: maccman-flarevideo-1.2-3-gf7b96fc.zip
URL: http://flarevideo.com/
Requires: oxzilla, flash-plugin
BuildArch: noarch

%description
* HTML5 video with Flash fallback
* Easy CSS/HTML/JS customization and theming
* Full screen support
* Completely open source and free for commercial use

%prep
%setup -q -n maccman-flarevideo-f7b96fc
sed -i -e "s|'http://flarevideo.com/flarevideo/examples/volcano.mp4'|location.search.substr(1,location.search.length)|" -e '/type:/d' index.html

%build

%install
rm -rf $RPM_BUILD_ROOT

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/bash
_URL=\$(readlink -f \$1)
cd %{_datadir}/%{name}
oxzilla -s 920x600 index.html?"\$_URL"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Nov 17 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial build
