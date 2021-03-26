Name:		liogo
Version:	0.4.1
Release:	46.1
Summary:	A Logo compiler for .NET
License:	GPL
Group:		Development/Languages
Source0:	http://sourceforge.net/projects/liogo/files/%{name}/%{version}/%{name}-%{version}-src-win32.zip
Source1:	%{name}.png
URL:		http://liogo.sourceforge.net/
BuildRequires:	mono-devel, nant, mono-winforms, mono-nunit
BuildRequires:	libgdiplus-devel
BuildArch:	noarch

%description
Most notable features of LIOGO are:
* UCBLogo compatibility,
* Framework of more than 200 Logo procedures,
* Turtle graphics Framework,
* Compile to EXE or dynamically loadable DLL,
* Liogo can call any .NET Assembly using any .NET language (C#, VB.NET, C++, ...),
* Use Logo variable scope (called can see calling variable),
* Include Logo dynamic operation (RUN, MAP, INVOKE, FOREACH, ...),
* Multi-thread core,
* Multi OS Support: Windows and Linux,
* Localization of structural element, framework and messages,
* OLE Automation interface to call Liogo from Excel, VBScript, ...
* Totally Free and Open Source (under GPL License).

%prep
%setup -q -n %{name}
sed -i 's|\.\.\\\\|../|g' */*.cs */*/*.cs
mkdir -p LIOGO-LANG/bin/Release/en LIOGO-LANG/bin/Release/fr LIOGO-LANG/bin/Release/de
sed -i '88i <include name="System.Windows.Forms.dll"/><include name="System.Configuration.dll"/>' LIOGO.build
sed -i '217i <include name="System.Windows.Forms.dll"/>' LIOGO.build

%build
nant build-lang build-core build-framework jay-compiler build-compiler build-ole build-guiwinbase build-liogoc build-liogoi || true
nant build-guiwpf || nant build-test || nant build-gacinstall || true

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
cd LIOGO-LANG/bin/Release;%__cp -a liogo-lang.dll en fr de $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGO-CORE/bin/Release;%__cp -a liogo-core.dll $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGO-FRAMEWORK/bin/Release;%__cp -a liogo-framework.dll $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGO-COMPILER/bin/Release;%__cp -a liogo-compiler.dll $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGO-OLE/bin/Release;%__cp -a liogo-ole.dll $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGO-GUI-WINBASE/bin/Release;%__cp -a liogo-gui-winbase.dll $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGOC/bin/Release;%__cp -a liogoc.exe $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..
cd LIOGOI/bin/Release;%__cp -a liogoi.exe $RPM_BUILD_ROOT%{_datadir}/%{name};cd ../../..

# script
%__mkdir_p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name}i << EOF
#!/bin/sh
export LIOGOPATH=%{_datadir}/%{name}
cd \$LIOGOPATH
mono %{name}i.exe
EOF

# freedesktop.org menu entry
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}i.desktop <<EOF
[Desktop Entry]
Name=Liogo
Comment=A Logo compiler for .NET
Exec=%{name}i
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Development;
EOF

%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc *.txt
%attr(0755,root,root) %{_bindir}/%{name}i
%{_datadir}/%{name}
%{_datadir}/applications/%{name}i.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Jun 26 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
