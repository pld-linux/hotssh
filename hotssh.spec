Summary:	Hotwire Shell - user interface for SSH secure shell
Summary(pl.UTF-8):	Hotwire Shell - interfejs użytkownika do bezpiecznej powłoki SSH
Name:		hotssh
Version:	0.2.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/hotssh/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	28de18a7cd158d14542acc08536d627c
URL:		https://wiki.gnome.org/Apps/HotSSH
BuildRequires:	python >= 1:2.4.2
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	openssh-clients
Requires:	python >= 1:2.4.2
Requires:	python-dbus
Requires:	python-pygobject >= 2
Requires:	python-pygtk-gtk >= 2:2
Requires:	python-pygtk-pango >= 2:2
Requires:	python-vte0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HotSSH is an interface to Secure Shell, for GNOME and OpenSSH. It
intends to be a better experience than simply invoking "ssh" from an
existing terminal window.

%description -l pl.UTF-8
HotSSH to interfejs do bezpiecznej powłoki, integrujący GNOME i
OpenSSH. Celem jest osiągnięcie lepszych doznań niż przy zwykłym
uruchomieniu "ssh" z istniejącego okna terminala.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc MAINTAINERS NEWS
%attr(755,root,root) %{_bindir}/hotssh
%dir %{py_sitedir}/hotssh
%{py_sitedir}/hotssh/*.py[co]
%dir %{py_sitedir}/hotssh/hotlib
%{py_sitedir}/hotssh/hotlib/*.py[co]
%dir %{py_sitedir}/hotssh/hotlib_ui
%{py_sitedir}/hotssh/hotlib_ui/*.py[co]
%dir %{py_sitedir}/hotssh/hotvte
%{py_sitedir}/hotssh/hotvte/*.py[co]
%{_desktopdir}/hotssh.desktop
%{_iconsdir}/hicolor/*/apps/hotwire-openssh.png
