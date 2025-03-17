%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

%define api	1.0
%define major	10
%define libname	%mklibname gdict %{api} %{major}
%define devname	%mklibname -d gdict %{api}

Summary:	GNOME Dictionary
Name:		gnome-dictionary
Version: 40.0
Release: 9
Epoch:   1
License:	GPLv2+ and LGPLv2
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-dictionary/%{url_ver}/%{name}-%{version}.tar.xz
# Upstream patch to fix build with meson 0.60+
Patch0:   https://gitlab.gnome.org/GNOME/gnome-dictionary/-/commit/cf3f8a67cd6f3059c555ed9cf0f5fba10abb7f68.patch
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	meson
BuildRequires:  docbook-xsl
BuildRequires:	libxml2-utils
Conflicts:	gnome-utils < 1:3.3.2

%description
GNOME Dictionary - Look up words in dictionary sources.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME dictionary shared library

%description -n %{libname}
This is the shared library required by the GNOME Dictionary.

%package -n %{devname}
Group:		Development/C
Summary:	GNOME dictionary library development files
Requires:	%{libname} = %{EVRD}
Provides:	libgdict%{api}-devel = %{EVRD}

%description -n %{devname}
This is the shared library required by the GNOME Dictionary.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc NEWS README.md
%{_bindir}/%{name}
%{_datadir}/gdict-%{api}/
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/metainfo/org.gnome.Dictionary.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_mandir}/man1/%{name}.1.*
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Dictionary.Devel.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Dictionary.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Dictionary-symbolic.svg

%files -n %{libname}
#{_libdir}/libgdict-%{api}.so.%{major}*

%files -n %{devname}
#doc #{_datadir}/gtk-doc/html/gdict/
#{_libdir}/libgdict-%{api}.so
#{_libdir}/pkgconfig/gdict-%{api}.pc
#{_includedir}/gdict-%{api}

