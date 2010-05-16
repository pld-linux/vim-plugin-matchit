Summary:	extended % matching for HTML, LaTeX, and many other languages
Summary(pl.UTF-8):	rozszerzone dopasowywanie % dla HTML, LaTeX-a i wielu innych języków
Name:		vim-plugin-matchit
Version:	1.13.2
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	matchit-%{version}.zip
# Source0-md5:	e1e416517e25c384bbaa1e7f5b1b650f
URL:		http://www.vim.org/scripts/script.php?script_id=39
BuildRequires:	unzip
Requires:	vim >= 4:7.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
The matchit.vim script allows you to configure % to match more than
just single characters. You can match words and even regular
expressions. Also, matching treats strings and comments (as recognized
by the syntax highlighting mechanism) intelligently.

The default ftplugins include settings for several languages: Ada, ASP
with VBS, Csh, DTD, Essbase, Fortran, HTML, JSP (same as HTML), LaTeX,
Lua, Pascal, SGML, Shell, Tcsh, Vim, XML. (I no longer keep track, so
there may be others.)

%description -l pl.UTF-8
Skrypt matchit.vim pozwala na skonfigurowanie % tak by potrafił
dopasować więcej niż jeden znak. Możliwe jest dopasowanie słów lub
wyrażeń regularnych, dodatkowo skrypt ten umożliwia inteligentne
przetwarzanie (za pomocą mechanizmu podświetlania składni) komentarzy
i łańcuchów znaków.

Domyślne wtyczki typów plików udostępniają wsparcie dla wielu języków:
Ada, ASP z VBS, Csh, DTD, Essbase, Fortran, HTML, JSP (tak samo jak
HTML), LaTeX, Lua, Pascal, SGML Shell, Tcsh, Vim, XML i inne.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}
cp -a doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
if [ "$1" = 0 ]; then
	umask 022
	echo ':helptags %{_vimdatadir}/doc' | vim -e -s
fi

%files
%defattr(644,root,root,755)
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
