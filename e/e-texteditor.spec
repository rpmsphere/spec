Name:		e-texteditor
Version:	1.0.35
Release:	180709%{?dist}.bin
Summary:	a fast and elegant text editor with many innovative features
Source0:	e-1.0-35-180709-x86.deb
Source1:	%{name}.png
#git clone git://github.com/etexteditor/e.git
URL:		http://e-texteditor.com/
Group:		Applications/Editors
License:	Open Company License
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
#BuildRequires:	wxGTK-devel glib2-devel atk-devel libcurl-devel libtomcrypt-devel libtommath-devel

%description
E is a new text editor with powerful editing features and quite a few
unique abilities. It makes manipulating text fast and easy, and lets
you focus on your writing by automating all the manual work. You can
extend it in any language, and by supporting TextMate bundles, it allows
you to tap into a huge and active community.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}
tar xzvf data.tar.gz

%__install -d %{buildroot}%{_datadir}/%{name}
cp -R opt/e/* %{buildroot}%{_datadir}/%{name}

%__install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_datadir}/%{name}
./e
EOF

%__install -d %{buildroot}%{_datadir}/applications
cat > %buildroot%_datadir/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=E Text Editor
Name[zh_TW]=易編輯器
Comment=a fast and elegant text editor with many innovative features
Comment[zh_TW]=快速、優雅又具有許多特色的文字編輯程式
Icon=%{name}
Categories=Application;Utility;Editor;
Exec=%{name}
Terminal=false
Type=Application
EOF

%__install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Fri Jul 24 2009 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.35-1.ossii.bin
- Initial package
