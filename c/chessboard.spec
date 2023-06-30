%define pkg_name ChessBoard

Name:           chessboard
Version:        2.05
Release:        1
Summary:        A Python implementation of the FIDE laws of chess
Group:          Amusements/Games
License:        GPL
URL:            https://arainyday.se/projects/python/%{pkg_name}/
Source:         https://arainyday.se/projects/python/%{pkg_name}/%{pkg_name}_%{version}.tar.gz
Source1:	%{name}.png
Requires:	pygame
BuildArch:	noarch

%description
The main goal is to implement all applicable rules in a simple,
straightforward way. The intention is not to be fast but to be easy
to understand and to be complete. Many other implementation has known
problems with castling, stalemate or other more or less special rules.

%prep
%setup -q -n %{pkg_name}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -a *.py img $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{pkg_name}
Name[zh_TW]=西洋棋盤
Comment=A Python implementation of the FIDE laws of chess
Comment[zh_TW]=以 Python 編寫的西洋棋盤
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;
EOF

#Exec
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
python2 ChessClient.py
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt HowToUseChessBoard.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.05
- Rebuilt for Fedora
